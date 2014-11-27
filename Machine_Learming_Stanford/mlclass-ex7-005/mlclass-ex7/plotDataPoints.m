function plotDataPoints(X, idx, K)
%PLOTDATAPOINTS plots data points in X, coloring them so that those with the same
%index assignments in idx have the same color
%   PLOTDATAPOINTS(X, idx, K) plots data points in X, coloring them so that those 
%   with the same index assignments in idx have the same color

% Create palette
palette = hsv(K + 1);
colors = palette(idx, :);

% Plot the data
scatter(X(1:100,1), X(1:100,2), 15, colors(1:100,:));
scatter(X(101:200,1), X(101:200,2), 15, colors(101:200,:));
scatter(X(201:300,1), X(201:300,2), 15, colors(201:300,:));

end
