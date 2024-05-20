import Sortable from "sortablejs";
import Alpine from "alpinejs";
import htmx from "htmx.org";

Alpine.data("sortList", () => ({
  init() {
    const rootElement = this.$el;
    const sortable = Sortable.create(rootElement, {
      animation: 150,

      onEnd: function (evt) {
        var itemElement = evt.item;
        const { id, csrf } = itemElement.dataset;
        htmx.ajax("PATCH", `/api/v1/comments/${id}/position`, {
          values: {
            newIndex: evt.newIndex,
          },
          headers: {
            "X-CSRFToken": csrf,
          },
          swap: "none",
        });
      },
    });
  },
}));
