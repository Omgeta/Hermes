let darkIcon, lightIcon, themeText
const currTheme = localStorage.getItem('theme') || (localStorage.setItem("theme", "light"), "light")
document.documentElement.setAttribute("theme", currTheme)

function displayThemeIcon() {
    const currTheme = localStorage.getItem('theme')
    
    if (currTheme === "dark") {
        darkIcon.setAttribute("display", "none")
        lightIcon.setAttribute("display", "block")
        themeText.innerHTML = "Light"
    } else if (currTheme === "light") {
        darkIcon.setAttribute("display", "block")
        lightIcon.setAttribute("display", "none")
        themeText.innerHTML = "Dark"
    }
}

function toggleTheme() {
    const currTheme = localStorage.getItem('theme')
    const nextTheme = currTheme === "light" ? "dark" : "light"
    
    localStorage.setItem('theme', nextTheme)
    document.documentElement.setAttribute("theme", nextTheme)
    displayThemeIcon()
}

window.onload = () => {
    darkIcon = document.getElementById("darkIcon")
    lightIcon = document.getElementById("lightIcon")
    themeText = document.getElementById("theme-text")
    document.getElementById("themeButton").onclick = toggleTheme
    displayThemeIcon()
}
