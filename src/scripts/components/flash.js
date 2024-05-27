import Alpine from "alpinejs"

Alpine.data("flash_message", () => ({
  show: true,

  close() {
    this.show = false
  },
}))
