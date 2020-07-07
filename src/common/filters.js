export function capitalize(value) {
  if (!value) return ''
  value = value.toString()
  return value.charAt(0).toUpperCase() + value.slice(1)
}

export function intcomma(value) {
  if (!value) return ''
  value = value.toString()
  return value.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
}
