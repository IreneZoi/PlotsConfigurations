#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TMath.h"
#include "TGraph.h"
#include "TVector2.h"
#include "TSystem.h"
#include "TLorentzVector.h"

#include <cmath>
#include <string>
#include <unordered_map>
#include <iostream>
#include <stdexcept>
#include <tuple>

//see https://github.com/UniMiBAnalyses/PlotsConfigurations/blob/VBSjjlnu/Configurations/VBSjjlnu/Full2017v6s5/macros/deltaphivars_class.cc for another example

using namespace std;

class VBSvar_Gen : public multidraw::TTreeFunction {
public: 
  VBSvar_Gen(char const* type);
  VBSvar_Gen(unsigned type);

  char const* getName() const override { return "VBSvar_Gen"; }
  TTreeFunction* clone() const override { return new VBSvar_Gen(returnVar_); }

  unsigned getNdata() override { return 6; }
  double evaluate(unsigned) override;

protected:
  enum ReturnType {
	                 mjj_vbs,
                   detajj_vbs,
                   eta0_vbs,
                   eta1_vbs,
                   pt0_vbs,
                   pt1_vbs,
                   nVarTypes
  };
  

void bindTree_(multidraw::FunctionLibrary&) override;

  unsigned returnVar_{nVarTypes};
 
  UIntValueReader* run{};
  UIntValueReader* luminosityBlock{};
  ULong64ValueReader* event{}; 

  static std::tuple<UInt_t, UInt_t, ULong64_t> currentEvent;
  static UIntValueReader* nGenJets; 
  static FloatArrayReader* GenJet_pt;
  static FloatArrayReader* GenJet_eta;
  static FloatArrayReader* GenJet_phi;
  static FloatArrayReader* GenJet_mass;


  static std::array<double, nVarTypes> returnValues;

  static void setValues(UInt_t, UInt_t, ULong64_t);
};


std::tuple<UInt_t, UInt_t, ULong64_t> VBSvar_Gen::currentEvent{};
UIntValueReader* VBSvar_Gen::nGenJets; 
FloatArrayReader* VBSvar_Gen::GenJet_pt{};
FloatArrayReader* VBSvar_Gen::GenJet_eta{};
FloatArrayReader* VBSvar_Gen::GenJet_phi{};
FloatArrayReader* VBSvar_Gen::GenJet_mass{};


std::array<double, VBSvar_Gen::nVarTypes> VBSvar_Gen::returnValues{};


VBSvar_Gen::VBSvar_Gen(char const* _type) :
  TTreeFunction()
{
  std::string type(_type);
  if (type == "mjj_vbs_Gen")
    returnVar_ = mjj_vbs;
  else if ( type == "detajj_vbs_Gen")
    returnVar_ = detajj_vbs;
  else if ( type == "eta0_vbs_Gen")
    returnVar_ = eta0_vbs;
  else if ( type == "eta1_vbs_Gen")
    returnVar_ = eta1_vbs;
  else if ( type == "pt0_vbs_Gen")
    returnVar_ = pt0_vbs;
  else if ( type == "pt1_vbs_Gen")
    returnVar_ = pt1_vbs; 
  else
    throw std::runtime_error("unknown return type " + type);
  
}

VBSvar_Gen::VBSvar_Gen(unsigned type) :
  TTreeFunction(),
  returnVar_(type) {}


double
VBSvar_Gen::evaluate(unsigned)
{
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
  return returnValues[returnVar_];
}

void
VBSvar_Gen::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");

    _library.bindBranch(nGenJets, "nGenJet");
    _library.bindBranch(GenJet_pt, "GenJet_pt");
    _library.bindBranch(GenJet_eta, "GenJet_eta");
    _library.bindBranch(GenJet_phi, "GenJet_phi");
    _library.bindBranch(GenJet_mass, "GenJet_mass");


    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {
                                     nGenJets = nullptr;
                                     GenJet_pt = nullptr;
                                     GenJet_eta = nullptr;
                                     GenJet_phi = nullptr;
                                     GenJet_mass = nullptr;
                                   });
}

/*static*/
void
VBSvar_Gen::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{

  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;

 currentEvent = std::make_tuple(_run, _luminosityBlock, _event);

  float Mjj_tmp=0;
  float Mjj_max=-9999.;
  unsigned int njet{*nGenJets->Get()};
  unsigned int vbs_0 = 0;
  unsigned int vbs_1 = 0;
  TLorentzVector jet0; 
  TLorentzVector jet1; 
  if (njet>=2){
    for (unsigned int ijet=0 ; ijet<njet ; ijet++){
      for (unsigned int jjet=0 ; jjet<njet ; jjet++){
        if (ijet==jjet) continue;
        jet0.SetPtEtaPhiM(GenJet_pt->At(ijet), GenJet_eta->At(ijet),GenJet_phi->At(ijet),GenJet_mass->At(ijet));   
        jet1.SetPtEtaPhiM(GenJet_pt->At(jjet), GenJet_eta->At(jjet),GenJet_phi->At(jjet),GenJet_mass->At(jjet)); 
        Mjj_tmp = (jet0 + jet1).M();
        if(Mjj_tmp>=Mjj_max){
          Mjj_max=Mjj_tmp;
          vbs_0 = ijet;
          vbs_1 = jjet;
        }
      }
      //deltaeta_vbs_Gen = 
    }
  }

  returnValues[mjj_vbs] = Mjj_max;
  returnValues[detajj_vbs] = GenJet_eta->At(vbs_0)-GenJet_eta->At(vbs_1);
  returnValues[eta0_vbs] = GenJet_eta->At(vbs_0);
  returnValues[eta1_vbs] = GenJet_eta->At(vbs_1);
  returnValues[pt0_vbs] = GenJet_pt->At(vbs_0);
  returnValues[pt1_vbs] = GenJet_pt->At(vbs_1);
}

