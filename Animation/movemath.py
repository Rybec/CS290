def _move_toward(source, dest, dist):
		''' Returns a point 'dist' tiles from 'source'
		in the direction of 'dest'

		This has all the hard vector math

		source -- tuple of x, y location of character
		dest   -- tuple of x, y location of destination
		dist   -- the distance in tiles moved from source

		If moving 'dist' will overshoot the destination,
		the returned value will be the destination itself.
		'''

		# Source location (where the character is)
		sx, sy = source

		# Destination
		dx, dy = dest

		# This is some vector math we need in
		# multiple places but only want to
		# calculate once.

		# Movement vector
		move_v = (dx - sx, dy - sy)
		# Unit vector divisor		
		u_divisor = math.sqrt(move_v[0]**2 + move_v[1]**2)
		# No reason to do the division twice
		scaling_factor = dist / u_divisor

		# New location
		if scaling_factor >= 1:
			# Don't want to overshoot it
			x, y = dx, dy
		else:
			x = sx + move_v[0] * scaling_factor
			y = sy + move_v[1] * scaling_factor

		return (x ,y)