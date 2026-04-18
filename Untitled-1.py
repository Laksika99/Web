<!DOCTYPE html>

<html lang="th">
<head>
<meta charset="UTF-8">
<title>Weather App</title>

<style>
body {
  font-family: sans-serif;
  background: linear-gradient(135deg, #667eea, #764ba2);
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  background: white;
  padding: 20px;
  border-radius: 12px;
  text-align: center;
  width: 300px;
}

input {
  width: 80%;
  padding: 8px;
  margin: 10px 0;
}

button {
  padding: 8px 16px;
}

.result {
  margin-top: 15px;
}
</style>

</head>

<body>

<div class="container">
  <h2>เช็คสภาพอากาศ</h2>

  <!-- ✅ ต้องมี input -->

  <input id="cityInput" placeholder="เช่น Bangkok" onkeypress="handleKeyPress(event)">

  <!-- ✅ ต้องมีปุ่ม -->

  <br>
  <button onclick="getWeather()">ค้นหา</button>

  <!-- ✅ ต้องมี result -->

  <div id="result" class="result"></div>
</div>

<script>
function handleKeyPress(event) {
  if (event.key === 'Enter') {
    getWeather();
  }
}

async function getWeather() {
  const city = document.getElementById("cityInput").value.trim();

  if (!city) {
    document.getElementById("result").innerHTML = "กรุณากรอกชื่อเมือง";
    return;
  }

  const apiKey = "e803f19d0146a8fae9d7da0841515f28";
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=th`;

  document.getElementById("result").innerHTML = "กำลังโหลด...";

  try {
    const res = await fetch(url);
    const data = await res.json();

    if (data.cod !== 200) {
      document.getElementById("result").innerHTML = "ไม่พบเมือง";
      return;
    }

    document.getElementById("result").innerHTML = `
      <h3>${data.name}</h3>
      <p>${data.main.temp} °C</p>
      <p>${data.weather[0].description}</p>
    `;
  } catch {
    document.getElementById("result").innerHTML = "error";
  }
}
</script>

</body>
</html>
