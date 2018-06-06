package main

import (
    "bytes"
    "os/exec"
)

// Run whois command and return buffer
func runWhoisCommand(query string) string {
    // Store output on buffer
    var out bytes.Buffer

    // Execute command
    cmd := exec.Command("whois", query)
    cmd.Stdout = &out
    cmd.Stderr = &out
    cmd.Run()

    return out.String()
}
