export function formatTime(time, cFormat) {
	if (arguments.length === 0) return null
	if ((time + '').length === 10) {
		time = +time * 1000
	}

	var format = cFormat || '{y}-{m}-{d} {h}:{i}:{s}',
		date
	if (typeof time === 'object') {
		date = time
	} else {
		date = new Date(time)
	}

	var formatObj = {
		y: date.getFullYear(),
		m: date.getMonth() + 1,
		d: date.getDate(),
		h: date.getHours(),
		i: date.getMinutes(),
		s: date.getSeconds(),
		a: date.getDay()
	}
	var time_str = format.replace(/{(y|m|d|h|i|s|a)+}/g, (result, key) => {
		var value = formatObj[key]
		if (key === 'a') return ['一', '二', '三', '四', '五', '六', '日'][value - 1]
		if (result.length > 0 && value < 10) {
			value = '0' + value
		}
		return value || 0
	})
	return time_str
}