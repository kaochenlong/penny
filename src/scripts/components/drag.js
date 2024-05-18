import { Sortable } from "@shopify/draggable";
import axios from "axios";
// import htmx from "htmx.org";

const sortable = new Sortable(document.querySelectorAll("#comments"), {
  draggable: ".comment-item",
});

sortable.on("sortable:stop", (e) => {
  const draggedElement = e.dragEvent.source;
  const { id, csrf } = draggedElement.dataset;

  if (e.oldIndex != e.newIndex) {
    axios.defaults.headers.common["X-CSRFToken"] = csrf;
    axios
      .post(`/api/v1/comments/${id}/position`, {
        newIndex: e.newIndex,
      })
      .then((response) => {
        console.log("成功");
      })
      .catch((error) => {
        console.error("Error deleting comment:", error);
      });

    // htmx.ajax("POST", `/api/v1/comments/${id}/position`, {
    //   values: {
    //     newIndex: newIndex,
    //   },
    //   headers: {
    //     "X-CSRFToken": csrf,
    //   },
    //   success: function (responseText) {
    //     console.log("位置更新成功");
    //   },
    //   error: function (error) {
    //     console.error("更新位置時發生錯誤:", error);
    //   },
    // });
  }
});
