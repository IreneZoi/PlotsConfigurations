void mergeScans(const char*  filename)
{
    TFile* f = new TFile(filename, "RECREATE");
    const int nChannels = 9;
    TString channels[nChannels] = {"all","res","boost","res_ele","res_mu","boost_ele","boost_mu","ele","mu"};
    TGraph* graph;
    for (int i =0; i < nChannels; i++)
    {
        TString lFilename = "2018_"+channels[i]+"_fit_v4.5.5/2018_"+channels[i]+"_split_Dipole_v4.5/scan_data.root";
        std::cout << " lFilename " << lFilename << std::endl;
        TFile* lf = new TFile(lFilename,"READ");
        graph = (TGraph*)lf->Get("scan_data");
        graph->SetName("2018_"+channels[i]+"_dipole_data");
        //graph->SetDirectory(0);
        f->cd();
        graph->Write();
        lf->Close();
    }
    f->Close();
}