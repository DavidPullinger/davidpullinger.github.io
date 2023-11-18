/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html"],
  theme: {
      extend: {
        colors: {
            primary: "#f2cc8f",
            secondary: "#DB6443",
            accent: "#81B29A",
        },
        screens: {
            '2xl': '2000px',
        },
      }
  },
  plugins: [],
}

