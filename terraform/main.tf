provider "vault" {
  version = "~> 2.0.0"
  address = var.address
  token   = var.token
}

resource "vault_pki_secret_backend" "pki" {
  path = var.path
}

resource "vault_pki_secret_backend_role" "client" {
  backend          = vault_pki_secret_backend.pki.path
  name             = var.roles.client
  allowed_domains  = var.domains
  allow_subdomains = true
  max_ttl          = 1 * 365 * 24 * 3600
  client_flag      = true
  server_flag      = false
  key_usage        = ["DigitalSignature"]
  ext_key_usage    = ["ClientAuth"]
  require_cn       = true
}

resource "vault_pki_secret_backend_role" "server" {
  backend          = vault_pki_secret_backend.pki.path
  name             = var.roles.server
  allowed_domains  = var.domains
  allow_subdomains = true
  max_ttl          = 5 * 365 * 24 * 3600
  client_flag      = false
  server_flag      = true
  key_usage        = ["DigitalSignature", "KeyEncipherment"]
  ext_key_usage    = ["ServerAuth"]
  require_cn       = true
}
