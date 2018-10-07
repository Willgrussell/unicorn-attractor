function sendMail(contactForm) {
    emailjs.send('gmail', 'unicorn_attractor', {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "issue_type": contactForm.issuetype.value,
        "issue_request": contactForm.issuesummary.value
    })
    .then(
        function(response){
            console.log("Success", response);
        },
        function(error) {
            console.log("Failed", error);
        });
        return false;  // To block from loading a new page
}