Tracker.module("PackagesApp.List", function (List, Tracker, Backbone, Marionette, $, _) {
  List.Controller = {
    listPackages: function () {
      var packages = Tracker.request("package:entities");
      var packagesListView = new List.Packages({
        collection: packages
      });
      Tracker.mainRegion.show(packagesListView);
    }
  };
});
