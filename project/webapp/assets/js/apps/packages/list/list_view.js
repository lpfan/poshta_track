Tracker.module("PackagesApp.List", function (List, Tracker, Backbone, Marionette, $, _) {
  List.Package = Marionette.ItemView.extend({
    tagName: "tr",
    template: "#package-list-item"
  });

  List.Packages = Marionette.CollectionView.extend({
    tagName: "table",
    className: "table table-hover",
    childView: List.Package
  });
});
