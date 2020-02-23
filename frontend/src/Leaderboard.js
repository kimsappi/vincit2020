import React from 'react';

class LeaderboardRow extends React.Component {
	render() {
		const row = this.props.row;
		const victories = Object.values(row.victories);
		const victoriesJSX = [];
		for (let victory of victories) {
			victoriesJSX.push(<td>{victory}</td>);
		}
		return (
			<tr>
				<td>{this.props.index}</td>
				<td>{row.username}</td>
				{victoriesJSX}
				<td>{row.resets}</td>
				<td>{row.points}</td>
			</tr>
		);
	}
}

class Leaderboard extends React.Component {
	render() {
		const leaderboard = this.props.leaderboard;
		const rows = [];
		for (let i = 0; i < leaderboard.length; ++i)
			rows.push(<LeaderboardRow index={i + 1} row={leaderboard[i]} />);
		const victories = Object.keys(leaderboard[0].victories);
		const victoriesJSX = [];
		for (let victory of victories) {
			victoriesJSX.push(<th>&#x1F3C6;{victory}</th>);
		}

		return (
			<table>
				<caption>Leaderboard</caption>
				<tr>
					<th>#</th>
					<th>User</th>
					{victoriesJSX}
					<th>Resets</th>
					<th>Score</th>
				</tr>
				{rows}
			</table>
		);
	}
}

export default Leaderboard;