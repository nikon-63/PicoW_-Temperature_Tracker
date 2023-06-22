<?php
if ($_SERVER["REQUEST_METHOD"] = "GET") {
        $temp = $_GET['temp'];
        $id = $_GET['id'];
        $date = date("Y/m/d");
        $time = date("h:i:sa");
        $Event = 1;

        $server = "<DB IP>";
        $user_name = "<DB Username>";
        $pass_word = "<DB Password>";
        $database = "<DB Database>";

        $conn = new mysqli($server, $user_name, $pass_word, $database);
        if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
        }


        $sql = "INSERT INTO heatingTracker (ID, Temperature, Time, Date, Event) VALUES ('$id', '$temp', '$time', '$date', '>
        if (mysqli_query($conn, $sql)) {
                echo "New record created successfully";
        } else {
                echo "Error: " . $sql . "<br>" . mysqli_error($conn);
        }

        mysqli_close($conn);
        }

?>
