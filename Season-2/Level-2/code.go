// Welcome to Secure Code Game Season-2/Level-2!

// Follow the instructions below to get started:

// 1. code_test.go is passing but the code is vulnerable
// 2. Review the code. Can you spot the bugs(s)?
// 3. Fix the code.go, but ensure that code_test.go passes
// 4. Run hack_test.go and if passing then CONGRATS!
// 5. If stuck then read the hint
// 6. Compare your solution with solution/solution.go

package main

import (
	"encoding/json"
	"log"
	"net/http"
	"regexp"
)

var reqBody struct {
	Email    string `json:"email"`
	Password string `json:"password"`
}

func isValidEmail(email string) bool {
	emailPattern := `^[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$`
	match, err := regexp.MatchString(emailPattern, email)
	if err != nil || !match {
		return false
	}
	return true
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
		return
	}

	testFakeMockUsers := map[string]string{
		"user1@example.com": "password12345",
		"user2@example.com": "B7rx9OkWVdx13$QF6Imq",
		"user3@example.com": "hoxnNT4g&ER0&9Nz0pLO",
		"user4@example.com": "Log4Fun",
	}

	if err := decodeRequestBody(r, &reqBody); err != nil {
		http.Error(w, "Cannot decode body", http.StatusBadRequest)
		return
	}

	if !isValidEmail(reqBody.Email) {
		log.Println("Invalid email format")
		http.Error(w, "Invalid email format", http.StatusBadRequest)
		return
	}

	if !authenticateUser(reqBody.Email, reqBody.Password, testFakeMockUsers) {
		http.Error(w, "Invalid Email or Password", http.StatusUnauthorized)
		return
	}

	log.Println("Successful login request")
	w.WriteHeader(http.StatusOK)
}

func decodeRequestBody(r *http.Request, target interface{}) error {
	decoder := json.NewDecoder(r.Body)
	decoder.DisallowUnknownFields()
	return decoder.Decode(target)
}

func authenticateUser(email, password string, users map[string]string) bool {
	storedPassword, exists := users[email]
	return exists && storedPassword == password
}

func main() {
	http.HandleFunc("/login", loginHandler)
	log.Println("Server started. Listening on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatalf("HTTP server ListenAndServe: %q", err)
	}
}
