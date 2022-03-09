recipient = document.getElementById("myemail")

function sendEmail() {
	Email.send({
	Host: "smtp.gmail.com",
	Username : "senderTFGemail@gmail.com",
	Password : "sendertfgemail",
	To : recipient,
	From : "senderTFGemail@gmail.com",
	Subject : "test",
	Body : "test",
	}).then(
		message => alert("mail sent successfully")
	);
}