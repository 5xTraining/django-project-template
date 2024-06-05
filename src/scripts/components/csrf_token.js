import Alpine from "alpinejs"

const CSRFToken = () => ({
  init() {
    Alpine.bind(this.$el, () => ({
      "@htmx:config-request.document"(evt) {
        const csrfToken = this.$el.content
        evt.detail.headers["X-CSRFToken"] = csrfToken
      },
    }))
  },
})

Alpine.data("csrf_token", CSRFToken)
