variable "address" {
  type = string
}

variable "token" {
  type = string
}

variable "path" {
  type    = string
  default = "pki_openvpn"
}

variable "domains" {
  type = list(string)
}

variable "roles" {
  type = object({
    client = string
    server = string
  })
}
