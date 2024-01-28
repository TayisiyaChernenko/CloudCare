/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte}'],
  theme: {
    colors: {
      'aa-dark-blue': '#0D73B1',
      'aa-blue': '#14ACDC',
      'aa-red': '#B61F23',
      'aa-grey': '#C7D0D7',
      'aa-white': '#FFFFFF',
      'aa-yellow': '#FFB800',
      'aa-green': '#30BA5F'
    },
    extend: {
      gridTemplateColumns: {
        '26': 'repeat(26, minmax(0, 1fr))',
      },
      gridColumn: {
        'span-26': 'span 26 / span 26',
      }
      
    },
  },
  plugins: [],
}

