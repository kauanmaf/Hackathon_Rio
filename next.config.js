module.exports = {
	async rewrites() {
		return [
			{
				source: '/api/:path*',
				destination: 'http://127.0.0.1:8000/api/:path*', // Assuming your Python backend runs on port 5000
			},
		]
	},
}