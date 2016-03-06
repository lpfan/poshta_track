Tracker.module("PackagesApp.List", function (List, Tracker, Backbone, Marionette, $, _) {
  List.Package = Marionette.ItemView.extend({
    tagName: "tr",
    template: "#package-list-item",

    events: {
      "click": "highlightBarcode",
      "click .js-delete-package": "deletePackage"
    },

    deletePackage: function(e) {
      e.stopPropagation();
      this.model.collection.remove(this.model);
    },

    highlightBarcode: function (e) {
      e.preventDefault();
      this.$el.toggleClass("warning");
    },

    remove: function () {
      this.$el.fadeOut();
    }

  });

  List.Packages = Marionette.CompositeView.extend({
    tagName: "table",
    className: "table table-hover",
    childView: List.Package,
    template: "#package-list",
    itemViewContainer: "tbody"
  });
});
