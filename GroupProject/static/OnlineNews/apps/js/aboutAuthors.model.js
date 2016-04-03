var app = angular.module("AboutAuthorsApp", []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.controller("AboutAuthorsController", function($scope) {
	$scope.authors = {};
	$scope.init = function() {
		// jsonData = $('#jsonData').val();
		$.ajax({
			url: "http://127.0.0.1:8000/getAuthors",
			type: "POST",
			data: {
				csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(),
			},
			success: function (jsonData) {
				$scope.authors = JSON.parse(jsonData);
				alert($scope.authors.Name);
				$scope.$apply();
			}
		});
	}
});
