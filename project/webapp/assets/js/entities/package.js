Tracker.module("Entities", function(Entities, Tracker, Backbone, Marionette, $, _){
  Entities.Package = Backbone.Model.extend({});

  Entities.PackageCollection = Backbone.Collection.extend({
    model: Entities.Package
  });

  var packages;

  var initializePackages = function () {
    packages = new Entities.PackageCollection([
      { 'id': 1, 'barcode': '0000001' },
      { 'id': 2, 'barcode': '0000002' },
      { 'id': 3, 'barcode': '0000003' }
    ]);
  };

  var API = {
    getPackageEntities: function () {
      if (packages === undefined ) {
        initializePackages();
      }
      return packages;
    }
  };

  Tracker.reqres.setHandler("package:entities", function () {
    return API.getPackageEntities();
  });
});
