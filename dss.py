@app.route('/clear_cache/<int:id>')
def clear_user_cache(id):
	cache.delete(f'user_data::{id}')
	return jsonify({'message': f'Cache for user {id} cleared'})

