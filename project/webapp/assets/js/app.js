var Tracker = new Marionette.Application();

Tracker.addRegions({
  mainRegion: "#main-region"
});
Tracker.on("start", function(){
    Tracker.PackagesApp.List.Controller.listPackages();
});
