package main

import (
	"fmt"
	"io"
	"net/http"
	"strings"
)

func whois(w http.ResponseWriter, r *http.Request) {
	domain := strings.Split(r.URL.Path, "/")[1]
	whoistext := runWhoisCommand(domain)
	io.WriteString(w, whoistext)
	fmt.Println(r.URL.Path)
	fmt.Println(domain)
	fmt.Println(whoistext)
}


func faviconHandler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "/opt/http_whois/favicon.ico")
}

func main() {
	http.HandleFunc("/", whois)
    http.HandleFunc("/favicon.ico", faviconHandler)
	http.ListenAndServe(":8080", nil)
}
